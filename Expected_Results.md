I have used the file; ./ML_Notebook/hdr_tf/"handwritten_digts_recognition_cnn_5layer.py" 

On running the python script for 50000 epochs, the following results were recorded.

Testing Accuracy: 94.53125


For debugging this file, two methods were adopted:
1. Tensorboard

Primarily, I used the Tensorboard to chart out a graph visualization of the CNN model and check the graph for consistency in dimensionality acoss layers.
Tensorboard also helps to interactively monitor the training process. 

Also, Tensorboard helps visualize the trend of various parameters during the training cycles.

The following screenshots indicate the various parameters obtained as results for the model: handwritten_digts_recognition_cnn_5layer.py

![graph_large_attrs_key _too_large_attrs limit_attr_size 1024 run](https://user-images.githubusercontent.com/23459946/45798706-d296dd80-bc78-11e8-90b3-ef36c6eb50d6.png)

This is the computatonal graph of the neural network used.

![accuracy cost](https://user-images.githubusercontent.com/23459946/45798748-f9edaa80-bc78-11e8-9419-db2c5639e503.png)

The above sreenshot illustrates the trend of accuracy and cost function with increasing training cycles.

Also, the distribution of weights can be seen in the below screenshot
![weight_dist](https://user-images.githubusercontent.com/23459946/45798887-8b5d1c80-bc79-11e8-91ab-8b8ec4141b06.png)


2. CLI TensorFlow debugger

To debug the code after every run through CLI (Command Line Interface), wrap the Session object with a debugger wrapper:
using the following:

from tensorflow.python import debug as tf_debug
sess = tf_debug.LocalCLIDebugWrapperSession(sess) ---> Opens a CLI environment,; type 'run' in the command line ---> Proceed to next Session.run() call (Essentially next epoch)

This opens the following window after first run:

![after_1step_run](https://user-images.githubusercontent.com/23459946/45799120-63ba8400-bc7a-11e8-82cf-debe04a461b1.png)

Type run again for the second run and the terminal will look like this:

![2_step_cli_debug](https://user-images.githubusercontent.com/23459946/45799185-a3816b80-bc7a-11e8-82d1-31b2406e851a.png)

Thus, tfdbg helps debug the code effectively.

