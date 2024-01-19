import json
import ruamel.yaml
import sys

def main():
    with open('include/testinput.json') as f:
        x = json.load(f)
        print(x)
        print('###########################################')
        yaml = ruamel.yaml.YAML()
        yaml.dump(x, sys.stdout)



if __name__ == '__main__':
    main()