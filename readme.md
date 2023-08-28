# Basic Pagerank Algorithm 
## Requirements
- Python 3.9+

## How to Run

You can run the algorithm with the following command:

```shell
python3 pagerank.py <input_data> <output_file> [parameters]
```

For `input_data` you should put the location of the text file with graph information. For `output_file` parameter you should define a file with path to get the results of the algorithm.


Other parameters are optional and each have default values.

### Parameters

- **teleportation:** This defines the teleportation of the algorithm. Default value: 0.10
- **threshold:** The threshold for the power iteration. Default value: 0.000001
- **max_iter:** The maximum number of iterations for the power iteration. Default value: 500

