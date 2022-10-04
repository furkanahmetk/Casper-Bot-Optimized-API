# Bot-Optimized-Validator-Api

## Introduction

Application backend for Bot-Optimized-Validator-Api



## How to set-up

Download and run the mongo db server from official website(https://www.mongodb.com/try/download/community)


Clone the repository.
```
git clone git_address
```

Configure src.config file according to mongo db port.
```
DEBUG = True
TESTING = False
MONGO_URI = 'mongodb://localhost:27017'
DB_NAME = 'bot_optimized'
```

To run project
```
make run
```

To test project
```
make test
```

