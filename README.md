# Django-Community-Forum-Website
A simple forum wesbite built with Django, an online discussion site where people can post questions, possts and interract with other users.

```
WebAppProject-Forum
├─ db.sqlite3
├─ main
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_category_description.py
│  │  ├─ 0003_auto_20210405_1520.py
│  │  ├─ 0004_auto_20210618_0224.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ 0001_initial.cpython-312.pyc
│  │     ├─ 0001_initial.cpython-39.pyc
│  │     ├─ 0002_category_description.cpython-312.pyc
│  │     ├─ 0002_category_description.cpython-39.pyc
│  │     ├─ 0003_auto_20210405_1520.cpython-312.pyc
│  │     ├─ 0003_auto_20210405_1520.cpython-39.pyc
│  │     ├─ 0004_auto_20210618_0224.cpython-312.pyc
│  │     ├─ 0004_auto_20210618_0224.cpython-39.pyc
│  │     ├─ __init__.cpython-312.pyc
│  │     └─ __init__.cpython-39.pyc
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ utils.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-312.pyc
│     ├─ admin.cpython-39.pyc
│     ├─ context_processors.cpython-312.pyc
│     ├─ context_processors.cpython-39.pyc
│     ├─ forms.cpython-312.pyc
│     ├─ forms.cpython-39.pyc
│     ├─ models.cpython-312.pyc
│     ├─ models.cpython-39.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ urls.cpython-39.pyc
│     ├─ utils.cpython-312.pyc
│     ├─ utils.cpython-39.pyc
│     ├─ views.cpython-312.pyc
│     ├─ views.cpython-39.pyc
│     ├─ __init__.cpython-312.pyc
│     └─ __init__.cpython-39.pyc
├─ manage.py
├─ media
│  └─ authors
│     ├─ cat-5852139_640.jpeg
│     ├─ man-156584_1280.apng
│     ├─ man-6259830_640.jpeg
│     ├─ pexels-pixabay-2204531.jpeg
│     └─ pexels-tomaz-barcellos-1987301.jpeg
├─ project
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ settings.cpython-312.pyc
│     ├─ settings.cpython-39.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ urls.cpython-39.pyc
│     ├─ wsgi.cpython-312.pyc
│     ├─ wsgi.cpython-39.pyc
│     ├─ __init__.cpython-312.pyc
│     └─ __init__.cpython-39.pyc
├─ README.md
├─ register
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ __init__.cpython-312.pyc
│  │     └─ __init__.cpython-39.pyc
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-312.pyc
│     ├─ admin.cpython-39.pyc
│     ├─ forms.cpython-312.pyc
│     ├─ forms.cpython-39.pyc
│     ├─ models.cpython-312.pyc
│     ├─ models.cpython-39.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ urls.cpython-39.pyc
│     ├─ views.cpython-312.pyc
│     ├─ views.cpython-39.pyc
│     ├─ __init__.cpython-312.pyc
│     └─ __init__.cpython-39.pyc
├─ requirements.txt
├─ static
│  ├─ admin
│  │  ├─ css
│  │  │  ├─ autocomplete.css
│  │  │  ├─ base.css
│  │  │  ├─ changelists.css
│  │  │  ├─ dashboard.css
│  │  │  ├─ fonts.css
│  │  │  ├─ forms.css
│  │  │  ├─ login.css
│  │  │  ├─ nav_sidebar.css
│  │  │  ├─ responsive.css
│  │  │  ├─ responsive_rtl.css
│  │  │  ├─ rtl.css
│  │  │  ├─ vendor
│  │  │  │  └─ select2
│  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │     ├─ select2.css
│  │  │  │     └─ select2.min.css
│  │  │  └─ widgets.css
│  │  ├─ fonts
│  │  │  ├─ LICENSE.txt
│  │  │  ├─ README.txt
│  │  │  ├─ Roboto-Bold-webfont.woff
│  │  │  ├─ Roboto-Light-webfont.woff
│  │  │  └─ Roboto-Regular-webfont.woff
│  │  ├─ img
│  │  │  ├─ calendar-icons.svg
│  │  │  ├─ gis
│  │  │  │  ├─ move_vertex_off.svg
│  │  │  │  └─ move_vertex_on.svg
│  │  │  ├─ icon-addlink.svg
│  │  │  ├─ icon-alert.svg
│  │  │  ├─ icon-calendar.svg
│  │  │  ├─ icon-changelink.svg
│  │  │  ├─ icon-clock.svg
│  │  │  ├─ icon-deletelink.svg
│  │  │  ├─ icon-no.svg
│  │  │  ├─ icon-unknown-alt.svg
│  │  │  ├─ icon-unknown.svg
│  │  │  ├─ icon-viewlink.svg
│  │  │  ├─ icon-yes.svg
│  │  │  ├─ inline-delete.svg
│  │  │  ├─ LICENSE
│  │  │  ├─ README.txt
│  │  │  ├─ search.svg
│  │  │  ├─ selector-icons.svg
│  │  │  ├─ sorting-icons.svg
│  │  │  ├─ tooltag-add.svg
│  │  │  └─ tooltag-arrowright.svg
│  │  └─ js
│  │     ├─ actions.js
│  │     ├─ actions.min.js
│  │     ├─ admin
│  │     │  ├─ DateTimeShortcuts.js
│  │     │  └─ RelatedObjectLookups.js
│  │     ├─ autocomplete.js
│  │     ├─ calendar.js
│  │     ├─ cancel.js
│  │     ├─ change_form.js
│  │     ├─ collapse.js
│  │     ├─ collapse.min.js
│  │     ├─ core.js
│  │     ├─ inlines.js
│  │     ├─ inlines.min.js
│  │     ├─ jquery.init.js
│  │     ├─ nav_sidebar.js
│  │     ├─ popup_response.js
│  │     ├─ prepopulate.js
│  │     ├─ prepopulate.min.js
│  │     ├─ prepopulate_init.js
│  │     ├─ SelectBox.js
│  │     ├─ SelectFilter2.js
│  │     ├─ urlify.js
│  │     └─ vendor
│  │        ├─ jquery
│  │        │  ├─ jquery.js
│  │        │  ├─ jquery.min.js
│  │        │  └─ LICENSE.txt
│  │        ├─ select2
│  │        │  ├─ i18n
│  │        │  │  ├─ af.js
│  │        │  │  │  ...
│  │        │  ├─ LICENSE.md
│  │        │  ├─ select2.full.js
│  │        │  └─ select2.full.min.js
│  │        └─ xregexp
│  │           ├─ LICENSE.txt
│  │           ├─ xregexp.js
│  │           └─ xregexp.min.js
│  ├─ aquire.otf
│  ├─ django_tinymce
│  │  └─ init_tinymce.js
│  ├─ hitcount
│  │  ├─ hitcount-jquery.js
│  │  └─ jquery.postcsrf.js
│  ├─ main.js
│  ├─ style.css
│  └─ tinymce
│     ├─ icons
│     │  └─ default
│     │     └─ icons.min.js
│     ├─ jquery.tinymce.min.js
│     ├─ langs
│     │  ├─ ar.js
│     │  │  ...
│     ├─ license.txt
│     ├─ plugins
│     │  ├─ advlist
│     │  │  └─ plugin.min.js
│     │  ├─ anchor
│     │  │  └─ plugin.min.js
│     │  ├─ autolink
│     │  │  └─ plugin.min.js
│     │  ├─ autoresize
│     │  │  └─ plugin.min.js
│     │  ├─ autosave
│     │  │  └─ plugin.min.js
│     │  ├─ bbcode
│     │  │  └─ plugin.min.js
│     │  ├─ charmap
│     │  │  └─ plugin.min.js
│     │  ├─ code
│     │  │  └─ plugin.min.js
│     │  ├─ codesample
│     │  │  └─ plugin.min.js
│     │  ├─ colorpicker
│     │  │  └─ plugin.min.js
│     │  ├─ contextmenu
│     │  │  └─ plugin.min.js
│     │  ├─ directionality
│     │  │  └─ plugin.min.js
│     │  ├─ emoticons
│     │  │  ├─ js
│     │  │  │  ├─ emojis.js
│     │  │  │  └─ emojis.min.js
│     │  │  └─ plugin.min.js
│     │  ├─ fullpage
│     │  │  └─ plugin.min.js
│     │  ├─ fullscreen
│     │  │  └─ plugin.min.js
│     │  ├─ help
│     │  │  └─ plugin.min.js
│     │  ├─ hr
│     │  │  └─ plugin.min.js
│     │  ├─ image
│     │  │  └─ plugin.min.js
│     │  ├─ imagetools
│     │  │  └─ plugin.min.js
│     │  ├─ importcss
│     │  │  └─ plugin.min.js
│     │  ├─ insertdatetime
│     │  │  └─ plugin.min.js
│     │  ├─ legacyoutput
│     │  │  └─ plugin.min.js
│     │  ├─ link
│     │  │  └─ plugin.min.js
│     │  ├─ lists
│     │  │  └─ plugin.min.js
│     │  ├─ media
│     │  │  └─ plugin.min.js
│     │  ├─ nonbreaking
│     │  │  └─ plugin.min.js
│     │  ├─ noneditable
│     │  │  └─ plugin.min.js
│     │  ├─ pagebreak
│     │  │  └─ plugin.min.js
│     │  ├─ paste
│     │  │  └─ plugin.min.js
│     │  ├─ preview
│     │  │  └─ plugin.min.js
│     │  ├─ print
│     │  │  └─ plugin.min.js
│     │  ├─ quickbars
│     │  │  └─ plugin.min.js
│     │  ├─ save
│     │  │  └─ plugin.min.js
│     │  ├─ searchreplace
│     │  │  └─ plugin.min.js
│     │  ├─ spellchecker
│     │  │  └─ plugin.min.js
│     │  ├─ tabfocus
│     │  │  └─ plugin.min.js
│     │  ├─ table
│     │  │  └─ plugin.min.js
│     │  ├─ template
│     │  │  └─ plugin.min.js
│     │  ├─ textcolor
│     │  │  └─ plugin.min.js
│     │  ├─ textpattern
│     │  │  └─ plugin.min.js
│     │  ├─ toc
│     │  │  └─ plugin.min.js
│     │  ├─ visualblocks
│     │  │  └─ plugin.min.js
│     │  ├─ visualchars
│     │  │  └─ plugin.min.js
│     │  └─ wordcount
│     │     └─ plugin.min.js
│     ├─ skins
│     │  ├─ content
│     │  │  ├─ dark
│     │  │  │  └─ content.min.css
│     │  │  ├─ default
│     │  │  │  └─ content.min.css
│     │  │  ├─ document
│     │  │  │  └─ content.min.css
│     │  │  └─ writer
│     │  │     └─ content.min.css
│     │  └─ ui
│     │     ├─ oxide
│     │     │  ├─ content.inline.min.css
│     │     │  ├─ content.min.css
│     │     │  ├─ content.mobile.min.css
│     │     │  ├─ fonts
│     │     │  │  └─ tinymce-mobile.woff
│     │     │  ├─ skin.min.css
│     │     │  └─ skin.mobile.min.css
│     │     └─ oxide-dark
│     │        ├─ content.inline.min.css
│     │        ├─ content.min.css
│     │        ├─ content.mobile.min.css
│     │        ├─ fonts
│     │        │  └─ tinymce-mobile.woff
│     │        ├─ skin.min.css
│     │        └─ skin.mobile.min.css
│     ├─ themes
│     │  ├─ mobile
│     │  │  └─ theme.min.js
│     │  └─ silver
│     │     └─ theme.min.js
│     └─ tinymce.min.js
├─ staticfiles
│  ├─ admin
│  │  ├─ css
│  │  │  ├─ autocomplete.css
│  │  │  ├─ base.css
│  │  │  ├─ changelists.css
│  │  │  ├─ dashboard.css
│  │  │  ├─ fonts.css
│  │  │  ├─ forms.css
│  │  │  ├─ login.css
│  │  │  ├─ nav_sidebar.css
│  │  │  ├─ responsive.css
│  │  │  ├─ responsive_rtl.css
│  │  │  ├─ rtl.css
│  │  │  ├─ vendor
│  │  │  │  └─ select2
│  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │     ├─ select2.css
│  │  │  │     └─ select2.min.css
│  │  │  └─ widgets.css
│  │  ├─ fonts
│  │  │  ├─ LICENSE.txt
│  │  │  ├─ README.txt
│  │  │  ├─ Roboto-Bold-webfont.woff
│  │  │  ├─ Roboto-Light-webfont.woff
│  │  │  └─ Roboto-Regular-webfont.woff
│  │  ├─ img
│  │  │  ├─ calendar-icons.svg
│  │  │  ├─ gis
│  │  │  │  ├─ move_vertex_off.svg
│  │  │  │  └─ move_vertex_on.svg
│  │  │  ├─ icon-addlink.svg
│  │  │  ├─ icon-alert.svg
│  │  │  ├─ icon-calendar.svg
│  │  │  ├─ icon-changelink.svg
│  │  │  ├─ icon-clock.svg
│  │  │  ├─ icon-deletelink.svg
│  │  │  ├─ icon-no.svg
│  │  │  ├─ icon-unknown-alt.svg
│  │  │  ├─ icon-unknown.svg
│  │  │  ├─ icon-viewlink.svg
│  │  │  ├─ icon-yes.svg
│  │  │  ├─ inline-delete.svg
│  │  │  ├─ LICENSE
│  │  │  ├─ README.txt
│  │  │  ├─ search.svg
│  │  │  ├─ selector-icons.svg
│  │  │  ├─ sorting-icons.svg
│  │  │  ├─ tooltag-add.svg
│  │  │  └─ tooltag-arrowright.svg
│  │  └─ js
│  │     ├─ actions.js
│  │     ├─ actions.min.js
│  │     ├─ admin
│  │     │  ├─ DateTimeShortcuts.js
│  │     │  └─ RelatedObjectLookups.js
│  │     ├─ autocomplete.js
│  │     ├─ calendar.js
│  │     ├─ cancel.js
│  │     ├─ change_form.js
│  │     ├─ collapse.js
│  │     ├─ collapse.min.js
│  │     ├─ core.js
│  │     ├─ inlines.js
│  │     ├─ inlines.min.js
│  │     ├─ jquery.init.js
│  │     ├─ nav_sidebar.js
│  │     ├─ popup_response.js
│  │     ├─ prepopulate.js
│  │     ├─ prepopulate.min.js
│  │     ├─ prepopulate_init.js
│  │     ├─ SelectBox.js
│  │     ├─ SelectFilter2.js
│  │     ├─ urlify.js
│  │     └─ vendor
│  │        ├─ jquery
│  │        │  ├─ jquery.js
│  │        │  ├─ jquery.min.js
│  │        │  └─ LICENSE.txt
│  │        ├─ select2
│  │        │  ├─ i18n
│  │        │  │  ├─ af.js
│  │        │  │  │  ...
│  │        │  ├─ LICENSE.md
│  │        │  ├─ select2.full.js
│  │        │  └─ select2.full.min.js
│  │        └─ xregexp
│  │           ├─ LICENSE.txt
│  │           ├─ xregexp.js
│  │           └─ xregexp.min.js
│  ├─ aquire.otf
│  ├─ django_tinymce
│  │  └─ init_tinymce.js
│  ├─ hitcount
│  │  ├─ hitcount-jquery.js
│  │  └─ jquery.postcsrf.js
│  ├─ main.js
│  ├─ style.css
│  └─ tinymce
│     ├─ icons
│     │  └─ default
│     │     └─ icons.min.js
│     ├─ jquery.tinymce.min.js
│     ├─ langs
│     ├─ license.txt
│     ├─ plugins
│     ├─ skins
│     │  ├─ content
│     │  │  ├─ dark
│     │  │  │  └─ content.min.css
│     │  │  ├─ default
│     │  │  │  └─ content.min.css
│     │  │  ├─ document
│     │  │  │  └─ content.min.css
│     │  │  └─ writer
│     │  │     └─ content.min.css
│     │  └─ ui
│     │     ├─ oxide
│     │     │  ├─ content.inline.min.css
│     │     │  ├─ content.min.css
│     │     │  ├─ content.mobile.min.css
│     │     │  ├─ fonts
│     │     │  │  └─ tinymce-mobile.woff
│     │     │  ├─ skin.min.css
│     │     │  └─ skin.mobile.min.css
│     │     └─ oxide-dark
│     │        ├─ content.inline.min.css
│     │        ├─ content.min.css
│     │        ├─ content.mobile.min.css
│     │        ├─ fonts
│     │        │  └─ tinymce-mobile.woff
│     │        ├─ skin.min.css
│     │        └─ skin.mobile.min.css
│     ├─ themes
│     │  ├─ mobile
│     │  │  └─ theme.min.js
│     │  └─ silver
│     │     └─ theme.min.js
│     └─ tinymce.min.js
└─ templates
   ├─ base.html
   ├─ create_post.html
   ├─ detail.html
   ├─ forums.html
   ├─ home.html
   ├─ latest-posts.html
   ├─ posts.html
   ├─ register
   │  ├─ signin.html
   │  ├─ signup.html
   │  └─ update.html
   └─ search.html

```