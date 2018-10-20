import glob

from PIL import Image
from PIL import ImageEnhance

NOTHING = ''
SPACE = ' '
BREAK_LINE = '\n'

BASE_TEMPLATE = '''
<link href="../canvas.css" rel="stylesheet" />
%(table)s
<script src="../canvas.js"></script>
'''

def export_html(path, image):
  width = image.width
  height = image.height

  table = [
    '''
    <table style="display: none" align="center" cellspacing="0">
    '''
  ]

  for x in range(width):
    table.append(
      '''
      <tr>
      '''
    )

    for y in range(height):
      coords = (x, y)
      [r, g, b, a] = image.getpixel(coords)
      table.append(
        '''
          <td style="background: rgba({r}, {g}, {b}, {a});">
            
          </td>
        '''.format(
          r=r,
          g=g,
          b=b,
          a=a,
        )
      )
    table.append(
      '''
      </tr>
      '''
    )

  table.append(
    '''
    </table>
    '''
  )

  with open(
    path
      .replace('will-be-processed', 'final')
      .replace('png', 'html'),
    'w'
  ) as file:
    file.write(
      BASE_TEMPLATE % {
        'table': NOTHING.join(table)
      }
    )


def main():
  multipier = 0.1

  for path in glob.glob('2018/will-be-processed/*.png'):
    image = Image.open(path)
    
    image.thumbnail((
      int(image.width * multipier),
      int(image.height * multipier)
    ))

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(3.0)

    export_html(path, image.rotate(90))

if __name__ == '__main__':
  main()
