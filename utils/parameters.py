import argparse
def get_parser():
    parser = argparse.ArgumentParser(description='Hyperparameter tuning and selection')
    parser.add_argument('-c', default='DeepFwFM', type=str, help='Models: FM, DeepFwFM ...')
    parser.add_argument('-use_cuda', default=1, type=int, help='Use CUDA or not')
    parser.add_argument('-gpu', default=0, type=int, help='GPU id')
    parser.add_argument('-n_epochs', default=8, type=int, help='Number of epochs')
    parser.add_argument('-numerical', default=13, type=int, help='Numerical features, 13 for Criteo')
    parser.add_argument('-use_multi', default='0', type=int, help='Use multiple CUDAs')
    parser.add_argument('-use_logit', default=0, type=int, help='Use Logistic regression')
    parser.add_argument('-use_fm', default=0, type=int, help='Use FM module or not')
    parser.add_argument('-use_fwlw', default=0, type=int, help='If to include FwFM linear weights or not')
    parser.add_argument('-use_lw', default=1, type=int, help='If to include FM linear weights or not')
    parser.add_argument('-use_ffm', default=0, type=int, help='Use FFM module or not')
    parser.add_argument('-use_fwfm', default=1, type=int, help='Use FwFM module or not')
    parser.add_argument('-use_deep', default=1, type=int, help='Use Deep module or not')
    parser.add_argument('-num_deeps', default=1, type=int, help='Number of deep networks')
    parser.add_argument('-deep_nodes', default=400, type=int, help='Nodes in each layer')
    parser.add_argument('-h_depth', default=3, type=int, help='Deep layers')
    parser.add_argument('-prune', default=0, type=int, help='Prune model or not')
    parser.add_argument('-prune_r', default=0, type=int, help='Prune r')
    parser.add_argument('-prune_deep', default=1, type=int, help='Prune Deep component')
    parser.add_argument('-prune_fm', default=1, type=int, help='Prune FM component')
    parser.add_argument('-emb_r', default=1., type=float, help='Sparse FM ratio over Sparse Deep ratio')
    parser.add_argument('-emb_corr', default=1., type=float, help='Sparse Corr ratio over Sparse Deep ratio')
    parser.add_argument('-sparse', default=0.9, type=float, help='Sparse rate')
    parser.add_argument('-warm', default=10, type=float, help='Warm up epochs before pruning')
    parser.add_argument('-ensemble', default=0, type=int, help='Ensemble models or not')
    parser.add_argument('-embedding_size', default=10, type=int, help='Embedding size')
    parser.add_argument('-batch_size', default=2048, type=int, help='Batch size')
    parser.add_argument('-random_seed', default=42, type=int, help='Random seed')
    parser.add_argument('-learning_rate', default=0.001, type=float, help='Learning rate')
    parser.add_argument('-momentum', default=0, type=float, help='Momentum')
    parser.add_argument('-l2', default=3e-7, type=float, help='L2 penalty')
    parser.add_argument('-dataset', default='criteo', type=str, help='Dataset to use', choices=['criteo', 'tiny-criteo', 'twitter'])
    parser.add_argument('-save_model_path', default=0, type=str, help='Saved model path')
    parser.add_argument('-dynamic_quantization', default=0, type=int, help='Apply dynamic network quantization')
    parser.add_argument('-static_quantization', default=0, type=int, help='Apply static network quantization')
    parser.add_argument('-quantization_aware', default=0, type=int, help='Quantization Aware Training')
    parser.add_argument('-kd', default=0, type=int, help='Perform knowledge distillation')
    parser.add_argument('-loss_type', default='logloss', type=str, help='Used loss (should be logloss but for kd we need softmax)')
    parser.add_argument('-embedding_bag', default=0, type=int, help='Use embedding bag')
    parser.add_argument('-qr_flag', default=0, type=int)
    parser.add_argument('-qr_operation', default="mult", type=str)
    parser.add_argument('-qr_collisions', default=4, type=int)
    parser.add_argument('-qr_threshold', default=200, type=int)
    parser.add_argument('-md_flag', default=0, type=int)
    parser.add_argument('-md_threshold', default=200, type=int)
    parser.add_argument('-twitter_category', default='like', type=str, choices=['reply', 'retweet', 'retweet_comment', 'like'])


    return parser