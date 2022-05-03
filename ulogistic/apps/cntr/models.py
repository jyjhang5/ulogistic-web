from django.db import models

class Imp(models.Model):
    vsl_seq = models.CharField(max_length=6)
    so_no = models.CharField(max_length=4)
    cntrno = models.CharField(max_length=11)
    vsl_cd = models.CharField(max_length=4)
    voyage = models.CharField(max_length=11)
    cntr_sz = models.CharField(max_length=2)
    erase_date = models.CharField(max_length=14, default=0)
    in_date = models.DateTimeField()
    out_date = models.DateTimeField(blank=True, null=True)

    class Meta():
        db_table = "import"
        unique_together = (('vsl_seq', 'so_no', 'cntrno'), )


class Exp(models.Model):
    vsl_seq = models.CharField(max_length=6)
    so_no = models.CharField(max_length=4)
    cntrno = models.CharField(max_length=11)
    vsl_cd = models.CharField(max_length=4)
    voyage = models.CharField(max_length=11)
    cntr_sz = models.CharField(max_length=2)
    erase_date = models.CharField(max_length=14, default=0)
    in_date = models.DateTimeField()
    ship_date = models.DateTimeField(blank=True, null=True)

    class Meta():
        db_table = "export"
        unique_together = (('vsl_seq', 'so_no', 'cntrno'), )


class Cntr(models.Model):
    cntrno = models.CharField(max_length=11)
    op_date = models.DateTimeField()
    op_cd = models.CharField(max_length=1)
    stus_cd = models.CharField(max_length=2)
    vsl_cd = models.CharField(max_length=4)
    voyage = models.CharField(max_length=11)
    so_no = models.CharField(max_length=4)
    pol = models.CharField(max_length=5)
    pod = models.CharField(max_length=5)
    seal_no = models.CharField(max_length=10)
    line_seal = models.CharField(max_length=15)
    vsl_seq = models.CharField(max_length=6)
    goss_wt = models.CharField(max_length=9)
    tare_wt = models.CharField(max_length=4)
    truk_wt = models.CharField(max_length=5)
    wt = models.CharField(max_length=9)
    truk_nm = models.CharField(max_length=20)
    truk_no = models.CharField(max_length=7)
    tran_pgm_id = models.CharField(max_length=20)
    owner = models.CharField(max_length=4)
    cntr_sz = models.CharField(max_length=2)
    erase_date = models.CharField(max_length=14, default=0)

    class Meta():
        db_table = 'cntr'
        unique_together = (('vsl_seq', 'cntrno'), )
