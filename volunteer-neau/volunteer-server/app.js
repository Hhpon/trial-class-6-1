const express = require("express")
const cors = require("cors")
const Volunteer = require("./model/volunteer")

const app = express()
app.use(cors())
app.use(express.static("public"))

app.get("/volunteer", async function (req, res) {
  console.log(req.query.key)
  const volunteers = await Volunteer.find({ studentId: req.query.key })
  res.send({ result: volunteers, pageIndex: volunteers.length })
})

app.listen(3000, () => {
  console.log("恭喜你成功搭建了一个志愿时长查询的服务器，请在网页中输入“localhost:3000/index.html”查看志愿时长")
})
