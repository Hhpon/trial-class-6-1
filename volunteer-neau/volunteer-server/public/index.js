var app = new Vue({
  el: "#app",
  data: {
    volunteers: [],
    key: "",
  },
  computed: {
    totalDuration() {
      return this.volunteers.reduce((prev, cur) => prev + cur.duration, 0)
    },
  },
  mounted() {
    this.getVolunteers()
  },
  methods: {
    getVolunteers() {
      axios.get("/volunteer", { params: { key: this.key } }).then((res) => {
        this.volunteers = res.data.result
      })
    },
  },
})
