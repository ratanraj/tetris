$(function(){
  var navigation = new Vue({
    el: '#navigation',
    created: function(){
      this.homePage();
    },
    methods: {
      hideAll: function(){
        $("#main-container .page").hide();
      },
      homePage: function(){
        this.hideAll();
        $("#homePage").show();
      },
      submissionsPage: function(){
        this.hideAll();
        $("#submissionsPage").show();
      },
      leaderBoardPage: function(){
        this.hideAll();
        $("#leaderBoardPage").show();
      }
    }
  });
  var submissions = new Vue({
    el:'#submissions',
    data: {
        submissions:[]
    },
    created: function(){
        this.fetchData()
        this.$watch('submissions', function(){
            //this.fetchData()
        })
      },
      methods: {
        fetchData: function() {
            var self=this;
            $.getJSON("/submissions",function(data){
                self.submissions=data;
                /*
                var progs = {}; 
                for(var i=0;i<data.length; i++) {
                    if(progs[data[i]['program']]==null) {
                        progs[data[i]['program']]=data[i];
                    }else if(progs[data[i]['program']]['time'] < data[i]['time']) {
                        progs[data[i]['program']]=data[i];
                    }
                }
                var _submissions = [];
                for(var i in progs) { _submissions.push(progs[i]) }
                self.submissions=_submissions;
                */
            });
        }
      }
  });
    var userscore = new Vue({
      el:'#userscore',
      data: {
        score:{},
      },
      created: function(){
        this.fetchData()
        this.$watch('score', function(){
            //this.fetchData()
        })
      },
      methods: {
        fetchData: function() {
            var self=this;
            $.getJSON("/userscore",function(data){
                self.score=data;
            });
        }
      }
  });
  var leaderboard = new Vue({
      el:'#leaderboard',
      data: {
        users:[],
      },
      created: function(){
        this.fetchData()
        this.$watch('users', function(){
            //this.fetchData()
        })
      },
      methods: {
        fetchData: function() {
            var self=this;
            $.getJSON("/scores",function(data){
                self.users=data;
            });
        }
      }
  });

  if(window.location.hash=='#home') {
    navigation.homePage()
  }else if(window.location.hash=='#submissions') {
    navigation.submissionsPage()
  }else if(window.location.hash=='#leaderboard') {
    navigation.leaderBoardPage()
  }
});


