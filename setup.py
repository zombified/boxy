from setuptools import setup


setup(
    app=['boxy.py'],
    name='Boxy',
    data_files=[],
    options={
        'py2app': {
            'argv_emulation': True,
            'iconfile': 'icon.icns',
            'plist': {
                'CFBundleShortVersionString': '0.2.0',
                'LSUIElement': True,
            },
            'packages': ['rumps'],
        }
    },
    setup_requires=['py2app'],
    install_requires=['rumps']
)
