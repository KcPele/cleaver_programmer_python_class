import datetime
import maya



now = maya.now()
tomorrow = maya.when('tomorrow')
print('This is todays date {} and this is for tomorrow{}'.format(now, tomorrow))
print(tomorrow.slang_date())