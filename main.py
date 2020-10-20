import argparse

parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('--file', action='store_true', help='action to perform ie: create|delete')
subparsers = parser.add_subparsers(help='sub-command help', dest="target")
# create the parser for the "a" command

# Functions

def create_variable(args):
    print("Handling variable")
    print(args)
    if args.action == "create":
        print(f"Creating var with name: {args.name} and repo: {args.repo} with value: {args.value}")
    elif args.action == "delete":
        print(f"Deleting var with name: {args.name} and repo: {args.repo} with value: {args.value}")
    elif args.action == "debug":
        print(f"Debugging var with name: {args.name} and repo: {args.repo} with value: {args.value}")
    else:
        print("Unknown action")

def create_keypair(args):
    print("Creating keypair")    
    print(args)
    if args.action == "create":
        print(f"Creating keypair with private_key_file: {args.private_key_file} and public_key_file: {args.public_key_file} in repo: {args.repo} ")
    elif args.action == "delete":
        print(f"Deleting keypair with private_key_file: {args.private_key_file} and public_key_file: {args.public_key_file} in repo: {args.repo}")      
    elif args.action == "debug":
        print(f"Debugging keypair with private_key_file: {args.private_key_file} and public_key_file: {args.public_key_file} in repo: {args.repo}")
    else:
        print("Unknown action")        

def create_conf(args):
    print("Creating config from yaml file")
    if args.action == "create":
        print(f"Creating content with config file: {args.file}in repo: {args.repo} with additional repos in file ")
    elif args.action == "delete":
        print(f"Deleting content with config file: {args.file}in repo: {args.repo} with additional repos in file ")
    elif args.action == "debug":
        print(f"Debugging content with config file: {args.file}in repo: {args.repo} with additional repos in file ")
    else:
        print("Unknown action")   


# Handle variables
parser_a = subparsers.add_parser(name="var", help='To Create variables')
parser_a.add_argument("--repo", type=str, help="Repo ie: my-git-repo-slug")
parser_a.add_argument('--name', type=str, help='name of the variable. Ex: --name MY_SUPER_VAR')
parser_a.add_argument("--value", type=str, help="value of the variable. EX: --value 'SOmething not that secret'")
parser_a.add_argument("--file", type=str, help="value of the variable. EX: --file random-file.enc.json | random-file.json")
parser_a.add_argument("--secured", type=bool, help="Should the variable be encrypted on bitbucket. Ex: --secured true")
parser_a.add_argument("action", choices=["create", "delete", "debug"], type=str, help="Action on variable Ex. create|delete")
parser_a.set_defaults(func=create_variable)

# create the parser for the "b" command
parser_b = subparsers.add_parser('keypair', help='keypair help')
# parser_b.add_argument('--private_key', help='Actual private file contents') # Test this with piping
# parser_b.add_argument('--public_key', , help='Actual public key file contents') # Test this with piping
parser_b.add_argument("action", choices=["create", "delete", "debug"], type=str, help="Action on variable Ex. create|delete")
parser_b.add_argument('--private_key_file', help='Sops encrypted private key file with *.enc.json postfix: Ex: --private_key_file: key.enc.x')
parser_b.add_argument('--public_key_file', help='Public key file. (No encryption support)')
parser_b.set_defaults(func=create_keypair)


parser_c = subparsers.add_parser('conf', help='config file help help')
parser_c.add_argument("action", choices=["create", "delete", "debug"], type=str, help="Action on variable Ex. create|delete")
parser_c.add_argument('--file', choices='XYZ', help='Config file containing custom yaml. Ex: --file my-configuration.yaml')
parser_c.add_argument('--repo', choices='XYZ', help='Additional repo to apply config to, will be appended repos defined in the yaml file spesified')
parser_c.set_defaults(func=create_conf)


# def handle_arguments_call_function(args):
#     print(vars(args))

args = None
try:
    print("Fakk")
    args = parser.parse_args()
    args.func(args)
    # handle_arguments_call_function(args)

except SystemExit as error:
    # logger.debug("No arguments given")

    parser.print_help()
    exit(1)
# logger.info("Choosing action to take")
# logger.info(f"{parser.action} chosen!")
# logger.info(f"{parser.private_key}")


# parse some argument lists
# parser.parse_args([ "-h"])
# parser.parse_args(["keypair", "-h"])
# parser.parse_args(["conf", "-h"])
# parser.parse_args(["-h"])
# parser.parse_args(["var", 'create', '--repo', "my-repo", "--name", "MY_VAR", "--value", "Text to add"])
# Namespace(bar=12, foo=False)
# parser.parse_args(['var', 'b', '--baz', 'Z'])
# Namespace(baz='Z', foo=True)