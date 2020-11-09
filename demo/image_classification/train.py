import paddle
import paddlehub as hub
import paddlehub.vision.transforms as T
from paddlehub.finetune.trainer import Trainer
from paddlehub.datasets import Flowers

if __name__ == '__main__':
    transforms = T.Compose([T.Resize((224, 224)), T.Normalize()])
    flowers = Flowers(transforms)
    flowers_validate = Flowers(transforms, mode='val')
    model = hub.Module(name='resnet50_vd_imagenet_ssld', label_list=["roses", "tulips", "daisy", "sunflowers", "dandelion"], load_checkpoint=None)
    optimizer = paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters())
    trainer = Trainer(model, optimizer, checkpoint_dir='img_classification_ckpt')
    trainer.train(flowers, epochs=100, batch_size=32, eval_dataset=flowers_validate, save_interval=10)