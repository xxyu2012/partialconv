def get_config():
    return  {
            ### EXECUTION SETTING ###
            # The using GPU ID
            'cuda_id': 0,
            # whether you use comet-ml for visualizing the training procedure
            'comet': False,
            # The Running mode ('train' or 'test')
            'mode': 'train',
            # fine-tuning
            'finetune': False,
            # The state path which you want to resume the training
            'resume': False,

            ### TRAINING PARAMETERS ###
            # the number of max iteration
            'max_iter': 5e+5,
            # the batch size
            'batch_size': 16,

            ### DATA AUGMENTATION ###
            # the mask augmentaiton flag
            'mask_augment': False,

            ### NETWORK SETTING ###
            # UNet layer size
            'layer_size': 7,

            ### LOSS PARAMETERS ###
            'valid_coef': 1.0,
            'hole_coef': 6.0,
            'tv_coef': 0.1,
            'perc_coef': 0.05,
            'style_coef': 120.0,
            # total variation calcuration method ('mean' or 'sum')
            'tv_loss': 'mean',

            ### OPTIMIZATION PARAMETERS ###
            'optim': 'Adam',
            'initial_lr': 2e-4,
            'finetune_lr': 5e-5,
            'momentum': 0,
            'weight_decay': 0,

            ### LOG INTERVALS ###
            # viaulizing the output images
            'vis_interval': 1000,
            # saving the model
            'save_model_interval': 50000,
            # printing the losses to standard output line
            'log_interval': 100,

            ### DIRECTORY PATH ###
            'data_root': 'data',
            'ckpt': 'ckpt',

            ### COMET ML SETTING ###
            'api_key': '',
            'project_name': '',
            'workspace': ''
            }
