const axios = require('axios');
const dotenv = require('dotenv')

dotenv.config();

const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.Guilds
    ],
});

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('messageCreate', async (message) => {
    if (!message?.author.bot){
        console.log('received a text: ' + message.content);

        let config = {
            method: 'get',
            maxBodyLength: Infinity,
            url: 'http://127.0.0.1:8000/mar',
            headers: { 
            'Content-Type': 'application/json'
            },
            data : JSON.stringify({
                "text": message.content
            })
        };

        if (message.content.startsWith("MAR")) {
            config.url = 'http://127.0.0.1:8000/img'
            axios.request(config)
                .then((res) => {
                    if ('error' in res.data) {
                        console.log(JSON.stringify(res.data.error));
                        message.channel.send(res.data.error);
                    }
                    else {
                        console.log(JSON.stringify(res.data.img));
                        message.channel.send(res.data.img);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        }
        else {
            axios.request(config)
                .then((res) => {
                    console.log(JSON.stringify(res.data.response));
                    message.channel.send(res.data.response);
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});

client.login(process.env.DISCORD_TOKEN);