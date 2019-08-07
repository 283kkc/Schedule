from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Staff(models.Model):
    name = models.CharField(verbose_name='名前', max_length=20, unique=True)
    wage = models.IntegerField(verbose_name='時給', blank=True)
    dayOfStart = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

class Entry(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='スタッフ')
    date = models.DateField(default=datetime.date.today)
    timeOfStart = models.DateTimeField(verbose_name='出勤時刻', null=True, blank=True)
    timeOfEnd = models.DateTimeField(verbose_name='退社時刻', null=True, blank=True)

    Break_Choice = (
        (0, 0), (15, 15), (30, 30), (45, 45), (60, 60), (75, 75), (90, 90),
    )
    timeOfBreak = models.IntegerField(verbose_name='休憩時間', default=0, choices=Break_Choice)

    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('staff', 'date')

    def timestamp(self, num):
        #出勤時間か、退勤時間をセット
        if num == 0:
            self.timeOfStart = timezone.now()
        elif num == 1:
            self.timeOfEnd = timezone.now()
        self.save()

    def approve(self):
        #管理者が出社記録を承認
        self.approved = True
        self.save()

    def __str__(self):
        return self.staff.name + '(' + str(self.date) + ')'