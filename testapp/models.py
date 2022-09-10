from django.db import models
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from strategy_field.fields import StrategyField
from strategy_field.registry import Registry

class AbstractPlan(object):

    def __init__(self, context):
        self.context = context

    def remaining_time(self):
        raise NotImplementedError


class SilverPlan(AbstractPlan):
    def __repr__(self):
        return "SilverPlan"

    def __str__(self):
        return "SilverPlan"

    def remaining_time(self, subscription_date):
        time_delta = timedelta(days=90)
        new_date = subscription_date + time_delta
        return new_date

class GoldPlan(AbstractPlan):

    def __repr__(self):
        return "GoldPlan"
    
    def __str__(self):
        return "GoldPlan"

    def remaining_time(self, subscription_date):
        time_delta = timedelta(days=180)
        new_date = subscription_date + time_delta
        return new_date

plan_registry = Registry(AbstractPlan)

plan_registry.register(SilverPlan)
plan_registry.register(GoldPlan)

class SampleUser(models.Model):
    business_plan = StrategyField(registry=plan_registry, blank =True)
    subscription_date = models.DateField(default=date.today,editable=True)
    username = models.CharField(max_length=64,null=True)