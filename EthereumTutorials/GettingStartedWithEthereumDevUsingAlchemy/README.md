# Getting Started with Ethereum Development Using Alchemy | Ethereum Tutorials

[Link](https://ethereum.org/en/developers/tutorials/getting-started-with-ethereum-development-using-alchemy/)

## Run

Insert Alchemy API key in `index.js`,

```
const alchemyAPIkey = "" // Set Alchemy API key here.
```

Build Docker image (from project dir),

```
docker build -t getting-started-with-ethereum-dev-using-alchemy .
```

Run `index.js` through Docker container,

```
docker run getting-started-with-ethereum-dev-using-alchemy node index.js
```

