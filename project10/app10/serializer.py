from rest_framework import serializers
from .models import Bank,Address_detail
# import re

class bankserializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields= "__all__"

    # def validate_bank_code(self, value):
    #     if not re.match(r'^\d{4}$', str(value)):
    #         raise serializers.ValidationError('Bank code must be a 4-digit number.')
    #     return value

    # def validate_account_number(self, value):
    #     if not re.match(r'^\d{6,}$', str(value)):
    #         raise serializers.ValidationError('Account number must be a 6-digit or more number.')
    #     return value

    # def validate_text_payer_id(self, value):
    #     if not re.match(r'^\d{9}$', str(value)):
    #         raise serializers.ValidationError('Text payer ID must be a 9-digit number.')
    #     return value

class addresserializer(serializers.ModelSerializer):

    class Meta:
        model=Address_detail
        fields= "__all__"
        # extra_kwargs = {
        #     "address": {
        #         "error_messages": {
        #             "write_only":True,
        #         },
        #     },
        #     "area": {
        #         "error_messages": {
        #             "required": "User's area is required",
        #         },
        #     },
        # }
    # def validate_email(self, value):
    #     if Address_detail.objects.filter(phone_number=value).exists():
    #         print(value)
    #         raise serializers.ValidationError("This phone number already exists!.")
    #     return value
    # # print(value)