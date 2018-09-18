# Neural Network Console CLI Demo

It's demonstation of how to use on local computer network and model created by [Neural Network Console](https://dl.sony.com).

## Usage

### Install anaconda3

You can install it from [Downloads - Anaconda](https://www.anaconda.com/download/#macos).

### Install nnabla

nnabla is python library of neural network developed by Sony. It's open source software licensed by Apache 2.0 License.

```
pip install nnabla
```

### Execute command

```
$ nnabla_cli forward -c result.nnp -d test.csv -o ./
2018-09-18 09:40:29,596 [nnabla][INFO]: Initializing CPU extension...
2018-09-18 09:40:30,211 [nnabla][INFO]: Parameter load (<built-in function format>): /var/folders/s3/q1g_r4fn0bj__vcwwk_kkg6m0000gp/T/tmpvxdt84bn/parameter.protobuf
2018-09-18 09:40:30,212 [nnabla][WARNING]: Old-style context. Updating to new format.
2018-09-18 09:40:30,213 [nnabla][WARNING]: Fallback to CPU context.
2018-09-18 09:40:30,220 [nnabla][INFO]: DataSource with shuffle(False)
2018-09-18 09:40:30,220 [nnabla][INFO]: Using DataSourceWithMemoryCache
2018-09-18 09:40:30,220 [nnabla][INFO]: DataSource with shuffle(False)
2018-09-18 09:40:30,229 [nnabla][INFO]: On-memory
2018-09-18 09:40:30,229 [nnabla][INFO]: Using DataIterator
2018-09-18 09:40:30,233 [nnabla][Level 99]: data 4 / 4
2018-09-18 09:40:30,234 [nnabla][Level 99]: Forward Completed.
```

### Check output

If y is closly 1.0, it's "9". If not, it's "4".

```
$ cat output_result.csv 
x:image,y'
/path/to/001.png,0.00019709873595274985
/path/to/002.png,1.0769620750750164e-08
/path/to/003.png,0.9999932050704956
/path/to/004.png,0.9113416075706482
```

## License

MIT.