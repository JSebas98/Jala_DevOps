import express from 'express';

const app = express();

// Ping => pong
app.get('/ping', (req, res) => {
    res.send('pong');
});

// Pong => ping
app.get('/pong', (req, res) => {
    res.send('ping');
});

const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`App listening on PORT ${port}`));

