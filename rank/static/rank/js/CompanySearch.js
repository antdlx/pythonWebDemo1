/**
 * Created by antdlx on 2016/10/23.
 */

//1、数据定义Ajax

json_data_list = eval("("+data_list+")");
var selecta="a1",selectb="b1",selectc="name",keyword="";
var options;


//2、返回DOM对象的通用函数
var g = function(id){
    if(id.substr(0,1)=="."){
        return document.getElementsByClassName(id.substr(1));
    }
    return document.getElementById(id);
}

//3、添加幻灯片的操作（所有幻灯片和对应的按钮）
function addLists(){
    //3.1 获取模板且删除多余的空格
    var tpl_main = g("template_list").innerHTML.replace(/^s*/,'').replace(/\s*$/,'');

    //3.2  定义最终输出的 HTML 变量
    var out_main = [];


    var index;

    index = json_data_list.length;

    for (var i = 0 ; i < index; i++){

        var _html_main = tpl_main.replace(/{ CompanyName }/g,json_data_list[i].name)
            .replace(/{ CompanyDescription }/g,json_data_list[i].status)
            .replace(/{ CompanyRegistTime }/g,json_data_list[i].registered_date)
            .replace(/{ CompanyArtificialPerson }/g,json_data_list[i].artificial_person)
            .replace(/{ CompanyLocation }/g,json_data_list[i].location)
            .replace(/{ CompanyWebsite }/g,json_data_list[i].info_url)


        out_main.push(_html_main);
    }

    //设置到list中并隐藏模板
    g('template_list_content').innerHTML = out_main.join("");
    $('#template_list').hide();
}

function updateList(json_data){
    $("#template_list_content").remove();
    $("<ul>").appendTo($(".listBox")).attr({"id":"template_list_content","class":"list-group"});
    json_data_list = json_data;
    addLists();
}

function initPages(){

    options = {
        bootstrapMajorVersion:3,
        alignment:"center",
        currentPage: CURRENT_PAGE_NUM,
        numberOfPages:10, //可显示出来的最大数量
        totalPages: TOTAL_PAGE_NUM,
        onPageClicked:function(event,originalEvent,type,page){

            switch (type) {
                case "first":
                    $.post("http://localhost:8000/getpages/",{"wantPageNum":1,"selecta":selecta,"selectb":selectb,"selectc":selectc,"keyword":keyword},function(data){
                        data = eval("("+data.data+")");
                        updateList(data);
                    });
                    CURRENT_PAGE_NUM = 1;
                    break;
                //上一页
                case "prev":
                    $.post("/getpages/",{"wantPageNum":CURRENT_PAGE_NUM-1,"selecta":selecta,"selectb":selectb,"selectc":selectc,"keyword":keyword},function(data){
                        data = eval("("+data.data+")");
                        updateList(data);
                    });
                    CURRENT_PAGE_NUM = CURRENT_PAGE_NUM-1;
                    break;
                case "next":

                    $.post("/getpages/",{"wantPageNum":CURRENT_PAGE_NUM+1,"selecta":selecta,"selectb":selectb,"selectc":selectc,"keyword":keyword},function(data){
                        data = eval("("+data.data+")");
                        updateList(data);
                    });
                    CURRENT_PAGE_NUM = CURRENT_PAGE_NUM+1;
                    break;
                case "last":
                    $.post("/getpages/",{"wantPageNum":TOTAL_PAGE_NUM,"selecta":selecta,"selectb":selectb,"selectc":selectc,"keyword":keyword},function(data){
                        data = eval("("+data.data+")");
                        updateList(data);
                    });
                    CURRENT_PAGE_NUM = TOTAL_PAGE_NUM;
                    break;
                case "page":
                    if(CURRENT_PAGE_NUM != page){
                        $.post("/getpages/",{"wantPageNum":page,"selecta":selecta,"selectb":selectb,"selectc":selectc,"keyword":keyword},function(data){
                            data = eval("("+data.data+")");
                            updateList(data);
                        });
                        CURRENT_PAGE_NUM = page;
                    }
                    break;
            }
        },
    };

    $('#pages').bootstrapPaginator(options);
}

function initHandlers(){
    $("#btn_a1").click(function(){
        selecta = "a1";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_a2").css({"background-color":"white","color":"black"});
        $("#btn_a3").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selecta":"a1"},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_a2").click(function(){
        selecta = "a2";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_a1").css({"background-color":"white","color":"black"});
        $("#btn_a3").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selecta":"a2"},function(data){

            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_a3").click(function(){
        selecta = "a3";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_a1").css({"background-color":"white","color":"black"});
        $("#btn_a2").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selecta":"a3"},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });


    $("#btn_b1").click(function(){
        selectb = "b1";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_b2").css({"background-color":"white","color":"black"});
        $("#btn_b3").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectb":"b1"},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_b2").click(function(){
        selectb = "开业";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_b1").css({"background-color":"white","color":"black"});
        $("#btn_b3").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectb":selectb},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_b3").click(function(){
        selectb = "存续";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_b1").css({"background-color":"white","color":"black"});
        $("#btn_b2").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectb":selectb},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });


    $("#btn_c1").click(function(){
        selectc = "name";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_c2").css({"background-color":"white","color":"black"});
        $("#btn_c3").css({"background-color":"white","color":"black"});
        $("#btn_c4").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectc":selectc},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_c2").click(function(){
        selectc = "score";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_c1").css({"background-color":"white","color":"black"});
        $("#btn_c3").css({"background-color":"white","color":"black"});
        $("#btn_c4").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectc":selectc},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_c3").click(function(){
        selectc = "registered_date";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_c1").css({"background-color":"white","color":"black"});
        $("#btn_c2").css({"background-color":"white","color":"black"});
        $("#btn_c4").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectc":selectc},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
    $("#btn_c4").click(function(){
        selectc = "registered_capital";
        $(this).css({"background-color": "blue","color":"white"});
        $("#btn_c1").css({"background-color":"white","color":"black"});
        $("#btn_c2").css({"background-color":"white","color":"black"});
        $("#btn_c3").css({"background-color":"white","color":"black"});
        $.post("/getpages/",{"wantPageNum":1,"selectc":selectc},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });


    $("#btn_search").click(function(){
        keyword = $("#keyword").val();
        $("#keyword").val("");
        $.post("/getpages/",{"wantPageNum":1,"keyword":keyword},function(data){
            json_data = eval("("+data.data+")");
            updateList(json_data);
            TOTAL_PAGE_NUM = eval("("+data.total_page_num+")");
            options.totalPages = TOTAL_PAGE_NUM;
            $("#pages").bootstrapPaginator(options);
        });
    });
}


//4、为了防止添加幻灯片是DOM对象还没有得到，所以我们需要在加载完之后再加载幻灯片
$(document).ready(function(){
    addLists();
    initPages();
    initHandlers();
});

