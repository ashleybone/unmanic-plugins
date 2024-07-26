
---

##### Plugin Settings:

###### <span style="color:blue">Apprise Push Notification URL(s)
</span>
A list of one or more Apprise URLs to which notifications will be sent when tasks are completed.

##### Documentation:

Push notifications are sent using the Apprise notifications library.  Apprise supports dozens of online notification
services such as Telegram, Discord, and Signal, application notifications such as Kodi and Nextcloud, desktop notifications,
and e-mail.

To send notifications to a desired service, a URL particular to that service must be specified.  The exact contents of
this URL depends on the service in question.

For instance, to send notifications via Telegram, a user must create a Telegram bot, then create a tgram URL using the bot token and your Telegram chat id.

By comparison, to send notifications via Discord, the user creates a channel for the notifications, enables webhooks, then creates the URL using the webhook ID and webhook token.

For detailed information on supported services and links to configure the services and construct the URLs, visit:
- [Apprise Documentation](https://github.com/caronc/apprise)

##### Example URLs:

- discord://4174216298/JHMHI8qBe7bk2ZwO5U711o3dV_js
- tgram://123456789:abcdefg_hijklmnop/12315544/
- kodi://user:password@kodihost.local
