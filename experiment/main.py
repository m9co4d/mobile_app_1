python
import cv2
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class CameraApp(App):
    def build(self):
        self.camera = cv2.VideoCapture(0)
        self.image = Image()

        # Обновление изображения каждые 1/30 секунды
        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return self.image

    def update(self, dt):
        ret, frame = self.camera.read()
        if ret:
            self.image.texture = self._frame_to_texture(frame)

    def _frame_to_texture(self, frame):
        buf = frame.tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        return texture

if __name__ == '__main__':
    CameraApp().run()



