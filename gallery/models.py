from django.db import models
from PIL import Image
import io
from django.core.files.uploadedfile import SimpleUploadedFile
import os


# from django.db.models.signals import pre_delete
# from django.dispatch.dispatcher import receiver

# Create your models here.


class Before (models.Model):
    name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to="thumbnails", editable=False, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self):
        img = Image.open(self.image)
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)

        temp_handle = io.BytesIO()
        img.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type='image/png')
        self.thumbnail.save(
            '%s_thumbnail%s' % (os.path.splitext(suf.name)[0], '.png'),
            suf, save=False
        )

        super(Before, self).save()

    def delete(self):
        try:
            os.remove(self.image.path)
            os.remove(self.thumbnail.path)
        except OSError as e:
            print("Failed with:", e.strerror)
            print("Error code:", e.code)

        super(Before, self).delete()

    # @receiver(models.signals.post_delete, sender=Before)
    # def auto_delete_file_on_delete(sender, instance, **kwargs):
    #     if instance.image:
    #         if os.path.isfile(instance.image.path):
    #             os.remove(instance.image.path)


class After (models.Model):
    name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='images')
    before = models.ForeignKey(Before)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails', editable=False, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self):
        img = Image.open(self.image)
        img.thumbnail((128, 128), Image.ANTIALIAS)

        temp_handle = io.BytesIO()
        img.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type='image/png')
        self.thumbnail.save(
            '%s_thumbnail%s' % (os.path.splitext(suf.name)[0], '.png'),
            suf, save=False
        )

        super(After, self).save()

    def delete(self):
        try:
            os.remove(self.image.path)
            os.remove(self.thumanail.path)
        except OSError as e:
            print("Failed with:", e.strerror)
            print("Error code:", e.code)

        super(After, self).delete()
