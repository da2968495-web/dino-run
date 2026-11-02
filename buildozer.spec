[app]

title = Dino Run

package.name = dinorun
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.permissions =

[buildozer]

log_level = 2
warn_on_root = 0
