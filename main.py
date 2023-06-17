import pygame


class GameEngine:
    def __init__(self, width, height, title):
        self.window = None
        self.width = width
        self.height = height
        self.title = title
        self.clock = pygame.time.Clock()
        self.is_running = False

    def initialize(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.is_running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        while self.is_running:
            self.window.update()

    def draw(self):
        pass

    def run(self):
        self.initialize()

        while self.is_running:
            self.handle_events()
            self.draw()
            self.update()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


class MyGame(GameEngine):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = None

    def initialize(self):
        super().initialize()
        self.player = Player()

    def update(self):
        self.player.update()

    def draw(self):
        self.player.draw()


class Player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.speed = 5
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, (self.x, self.y))


game = MyGame(600, 600, "My Game")
game.run()
