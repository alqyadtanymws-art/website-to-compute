const venom = require("venom-bot");

venom
  .create()
  .then((client) => start(client))
  .catch((erro) => {
    console.log(erro);
  });

function start(client) {
  client.onMessage(async (message) => {
    const text = message.body.toLowerCase();
    const sender = message.sender.id;

    if (text === "مرحبا") {
      await client.sendText(message.from, "أهلين ياوحش 😈🔥");
    }

    if (text.startsWith(".منشن") && message.isGroupMsg) {
      let chat = await client.getChatById(message.chatId);
      let mentions = chat.groupMetadata.participants.map(p => p.id._serialized);
      await client.sendMentioned(message.chatId, `القيادة تستدعي الجميع:\n`, mentions);
    }

    if (text === ".تفجير") {
      await client.sendText(message.from, "💥 تم التفجير بأمر القيادة");
    }
  });
}
