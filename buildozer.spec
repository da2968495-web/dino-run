[app]

title = Dino Run

package.name = dinorun
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 0
