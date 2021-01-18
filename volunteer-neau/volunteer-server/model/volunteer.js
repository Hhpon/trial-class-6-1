const mongoose = require("mongoose")

mongoose.connect("mongodb://localhost/trial-class", { useNewUrlParser: true, useUnifiedTopology: true })

const volunteerSchema = new mongoose.Schema({
  studentName: String,
  factory: String,
  classroom: String,
  studentId: String,
  org: String,
  service: String,
  duration: Number,
})

module.exports = mongoose.model("Volunteer", volunteerSchema)
