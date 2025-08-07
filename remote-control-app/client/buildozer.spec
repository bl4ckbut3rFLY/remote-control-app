[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_api = 21
android.archs = armeabi-v7a,arm64-v8a
android.build_tools_version = 36.0.0
android.allow_backup = False
android.logcat_filters = *:S python:D
android.enable_androidx = True
android.use_androidx = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.5.1
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
