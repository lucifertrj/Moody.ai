# Moody.ai
### Refresh your Mood
[![](https://images.unsplash.com/photo-1612878010854-1250dfc5000a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80)](https://unsplash.com/@tengyart)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://github.com/lucifertrj/Moody.ai/blob/v1.0/LICENSE)
[![PR](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/lucifertrj/Moody.ai/fork)

Real Time Facial Emotion Recognition and Movie or Song recommendation based on mood or emotion.

## Installation

### Using PIP

```python
pip install -r requirements.txt
```

### Using Docker

```python

```
## Running

**Linux and macOS**:

```bash
$ export FLASK_APP=hello
$ flask run
```

**Windows**:

```bash
> set FLASK_APP=hello
> flask run
```



## Dataset - FER-2013

<img src="https://miro.medium.com/max/1200/1*nXqJ4lMiBRp4Ilm3bpRxuA.png" alt="dataset">

The data consists of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centred and occupies about the same amount of space in each image.

The task is to categorize each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set consists of 28,709 examples and the public test set consists of 3,589 examples.


## CNN Architecture

```python
model= keras.models.Sequential()

model.add(keras.layers.Conv2D(32, (3,3), activation="relu",padding="same",input_shape=(48, 48, 3)))
model.add(keras.layers.Conv2D(32, (3,3), activation="relu",padding="same"))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Conv2D(64, (3,3), activation="relu",padding="same"))
model.add(keras.layers.Conv2D(64, (3,3), activation="relu",padding="same"))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.MaxPooling2D(2,2))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Conv2D(128, (3,3), activation="relu",padding="same"))
model.add(keras.layers.Conv2D(128, (3,3), activation="relu",padding="same"))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Dropout(0.25))

model.add(keras.layers.Conv2D(64, (3,3), activation="relu",padding="same"))
model.add(keras.layers.Conv2D(64, (3,3), activation="relu",padding="same"))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(512, activation="relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(7,activation="softmax"))
```
## Outcome

- User can first upload his selfie/Image, a Face Detection algorithm is run to detect Face and Resize it as per the model requirement
- If user is not feeling to upload a Image, he can choose his Mood through Radio Buttons.
- Now user can choose whether he needs Movie or Song Recommendation.
- Based on the detected mood, Recommendation of 5-6 Movies or Songs is recommended.

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.
## Feedback

If you have any feedback, please reach out to us at admin@animevyuh.org

## Contributors

- [Tarun R Jain](https://twitter.com/TRJ_0751)
- [Himanshu Agarwal](https://twitter.com/himture)
