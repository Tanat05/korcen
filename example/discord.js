const { check } = require("korcen");
const { MessageEmbed } = require("discord.js");

client.on("messageCreate", async (message) => {
  if (message.author.id === "") return; // 특정 유저 검사 무시
  const content = message.content;
  const c = check(content);

  if (c) {
    message.delete();
    message.channel.send({
      embeds: [
        new MessageEmbed()
          .setTitle("메세지 삭제함")
          .setFooter({ text: "디스코드 TNS 봇" }),
      ],
    });
  }
});
