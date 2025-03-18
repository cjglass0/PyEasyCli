class Renderer:
    def __init__(self):
        pass

class BasicRenderer(Renderer):
    def __init__(self):
        super().__init__()

        self.printer = None

    def render(self, lines):
        for line in lines:
            if self.printer:
                self.printer.print(line)
            else:
                print(line)