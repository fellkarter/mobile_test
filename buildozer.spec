[app]
title = Focus Breeze
package.name = focusbreeze
package.domain = org.focusbreeze
source.dir = .
source.include_exts = py,kv
version = 0.1
requirements = kivy
orientation = portrait
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 34
android.arch = armeabi-v7a
android.ndk = 25b
android.gradle_dependencies = 
android.permissions = INTERNET
android.minimum_api = 21

[test]
command = python -m pytest
