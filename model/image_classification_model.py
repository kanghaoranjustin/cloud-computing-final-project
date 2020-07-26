import mxnet as mx
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
from mxnet.gluon.data.vision import transforms
from mxnet.contrib.onnx.onnx2mx.import_model import import_model
import os




#mx.test_utils.download('https://s3.amazonaws.com/onnx-model-zoo/synset.txt')
with open('synset.txt', 'r') as f:
    labels = [l.rstrip() for l in f]



# Enter path to the ONNX model file
model_path= 'resnet18-v2-7.onnx'
sym, arg_params, aux_params = import_model(model_path)



Batch = namedtuple('Batch', ['data'])
def get_image(path, show=False):
    img = mx.image.imread(path)
    if img is None:
        return None
    if show:
        plt.imshow(img.asnumpy())
        plt.axis('off')
    return img

def preprocess(img):
    transform_fn = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    img = transform_fn(img)
    img = img.expand_dims(axis=0)
    return img


def predict(path):
    img = get_image(path, show=True)
    img = preprocess(img)
    mod.forward(Batch([img]))
    # Take softmax to generate probabilities
    scores = mx.ndarray.softmax(mod.get_outputs()[0]).asnumpy()
    # print the top-5 inferences class
    scores = np.squeeze(scores)
    a = np.argsort(scores)[::-1]
    return 'class=%s ; probability=%f' %(labels[a[0]],scores[a[0]])

# Determine and set context
if len(mx.test_utils.list_gpus())==0:
    ctx = mx.cpu()
else:
    ctx = mx.gpu(0)
# Load module
mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))],
         label_shapes=mod._label_shapes)
mod.set_params(arg_params, aux_params, allow_missing=True, allow_extra=True)


mx.test_utils.download('https://www.trafalgar.com/real-word/wp-content/uploads/sites/3/2019/10/giant-panda-750x400.jpg')

def get_image_class(image_link):
    mx.test_utils.download(image_link)
    img_path = image_link.split("/")[-1]
    return predict(img_path)


print(get_image_class('https://www.trafalgar.com/real-word/wp-content/uploads/sites/3/2019/10/giant-panda-750x400.jpg'))

