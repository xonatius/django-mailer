from django.contrib import admin
from mailer.models import Message, DontSendEntry, MessageLog

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_address', 'subject', 'when_added', 'priority')

class DontSendEntryAdmin(admin.ModelAdmin):
    list_display = ('to_address', 'when_added')

class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_address', 'subject', 'when_attempted', 'result')
    fields = ('to_address', 'from_address', 'subject', 'message_body', 'when_added', 'when_attempted', 'result')
    readonly_fields = fields

admin.site.register(Message, MessageAdmin)
admin.site.register(DontSendEntry, DontSendEntryAdmin)
admin.site.register(MessageLog, MessageLogAdmin)
