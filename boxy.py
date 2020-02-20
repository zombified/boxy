import rumps


INTERVAL = 1
DEFAULT_TITLE = "🌊"


class BoxyApp(rumps.App):
    def __init__(self):
        super(BoxyApp, self).__init__(
            type(self).__name__,
            title=DEFAULT_TITLE,
            menu=[
                "Start 60",
                "Start 25",
                "Start 5",
                "Stop",
            ])

        self.max_time = 60
        self.ticks = 0
        self.timer = None
        self.create_timer()
        #rumps.debug_mode(True)

    def create_timer(self):
        if self.timer is not None and self.timer.is_alive():
            self.timer.stop()
        self.timer = rumps.Timer(self.tick, INTERVAL)
        self.timer.stop()

    def tick(self, sender):
        self.ticks += 1
        if self.ticks >= self.max_time:
            self.timer.stop()
            self.time_done()
            return

        timeleft = self.max_time - self.ticks

        mins = timeleft // 60
        secs = timeleft - (60 * mins)
        self.title = "{:02d}:{:02d}".format(mins, secs)

    def time_done(self):
        self.title = DEFAULT_TITLE
        rumps.alert(
            title="Boxy",
            message="Hey! Times up!")
        rumps.notification(
            title="Boxy",
            subtitle="A message for you",
            message="Hey! Times up!",
            sound=True)

    @rumps.clicked("Start 60")
    def start_60(self, sender):
        self.max_time = 60 * 60
        self.ticks = 0
        self.timer.start()

    @rumps.clicked("Start 25")
    def start_25(self, sender):
        self.max_time = 60 * 25
        self.ticks = 0
        self.timer.start()

    @rumps.clicked("Start 5")
    def start_5(self, sender):
        self.max_time = 60 * 5
        self.ticks = 0
        self.timer.start()

    @rumps.clicked("Stop")
    def stop(self, sender):
        self.timer.stop()
        self.title = DEFAULT_TITLE


if __name__ == '__main__':
    app = BoxyApp()
    app.run()
