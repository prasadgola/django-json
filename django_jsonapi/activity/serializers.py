from rest_framework_json_api import serializers
from activity.models import User, ActivityPeriod

class UserSerializer(serializers.HperlinkedModelSerialilzer):
	class Meta:
		model = User
		fields = ('userid','real_name','tz')

class ActivityPeriodSerializer(serializers.HperlinkedModelSerialilzer):
	class Meta:
		model = DishSerializer
		fields = ('start_time','end_time')