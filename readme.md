= `sysd_minmon` Unit Monitor

`sysd_minmon` runs a script when selected systemd units change state (for example, 'activated' -> 'failed').  

It can be used with both system and user systemd instances.  The included dbus policy file is installed automatically but is only required for system unit monitoring.

=== Setup

Run `sudo pip2 install git+https://github.com/Rendaw/sysd_minmon`.

=== Command line

Run `sysd_minmon` to see command line arguments.

`sysd_minmon` calls the specified script with three positional command line arguments:
1. The service name (ex: `home.mount` or `webserver.service`)
2. The new state (ex: `failed`)
3. The scope (either `system` or `user`)

=== Running at startup
To run `sysd_minmon` at startup you can create a systemd service file following this template:

```
[Unit]
Description=Test monitoring some services

[Service]
Type=dbus
ExecStart=/usr/local/bin/sysd_minmon \
	/usr/bin/echo \
	my-btrfs.mount \
	my-btrfs-scrub.service \
	test-unit-failure.service
BusName=com.zarbosoft.sysd_minmon

[Install]
WantedBy=multi-user.target
```

Enable and start the service as usual.  You may wish to make this a `Requires` and `After` dependency of the watched services to ensure early failures aren't missed.

=== Testing

You can use this unit to test failure:
```
[Unit]
Description=Testing service failure and monitoring.  Everything is A-OK!

[Service]
Type=oneshot
ExecStart=/q
```

1. Save the unit as `test-unit-failure.service` in `/etc/systemd/system/` for system-instance testing, or `~/.config/systemd/user/` for user-instance testing.
2. Configure your `sysd_minmon` unit to watch `test-unit-failure.service`.  You may wish to use `/usr/bin/echo` as your script.
3. Run `systemctl start test-unit-failure.service` (or `systemctl --user start test-unit-failure.service` if testing a user-instance).
4. Confirm the monitor response script was run.  If you used `/usr/bin/echo`, check `journalctl --unit system-minmon.service` for `test-unit-failure.service failed system`.

