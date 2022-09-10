from rest_framework import serializers as rest_serializers
from .models import SampleUser,plan_registry
from .models import SilverPlan,GoldPlan


class StrategyFieldSerializer(rest_serializers.Field):
    def to_representation(self, value):
        return value.__class__.__name__
        
    def to_internal_value(self, data):
        x= [_CLS_.__name__ for _CLS_ in plan_registry]
        if data in x:
            return eval(data)
        else:
            raise ValueError(
                "Make sure you have sent the correct value for the business_plan field.The field contents are case-sensitive."
                )
        

class TestSerializer(rest_serializers.ModelSerializer):
    business_plan = StrategyFieldSerializer()
    class Meta:
        model = SampleUser
        fields = "__all__"
        
    def create(self, validated_data):
        new_user = SampleUser.objects.create(
            username=validated_data['username'],
            business_plan = validated_data['business_plan'],
            subscription_date = validated_data['subscription_date']
        )
        new_user.save()

        return new_user