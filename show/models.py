from django.db import models

# Create your models here.


class ksxx(models.Model):
    bkh = models.CharField(max_length=10, verbose_name="报名号")
    ksxm = models.CharField(max_length=6, verbose_name="考生姓名")
    ksbh = models.CharField(max_length=16, verbose_name="考生编号")
    zjhm = models.CharField(max_length=19, verbose_name="证件号码")
    bkdw = models.CharField(max_length=20, verbose_name="报考单位名称")
    kczw = models.CharField(max_length=20, verbose_name="考场座位")
    lh = models.CharField(max_length=20, verbose_name="楼号")
    kch = models.CharField(max_length=3, verbose_name="考场号")
    zwbh = models.CharField(max_length=3, verbose_name="座位编号")
    dyjs = models.CharField(max_length=10, verbose_name="对应教室")
    zydm = models.CharField(max_length=5, verbose_name="专业代码", blank=True, null=True)
    bkzy = models.CharField(max_length=10, verbose_name="报考单位名称", blank=True, null=True)

    def __unicode__(self):
        return ksxx.ksxm