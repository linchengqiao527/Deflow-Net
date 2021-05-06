package Sort;
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.awt.geom.Point2D;
import java.util.List;
import java.util.ArrayList;
public class MergeSort {
    static List<List<Point2D.Double>> pointslist = new ArrayList<List<Point2D.Double>>();
    public static void main(String[] args) {
       // printFile(new File("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data"));
        readshapeFileByLine("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\TAZ\\shp_point");
        printFile(new File("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data"));
        //readFileByLine("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data\\201901\\2019-01-01\\2019-01-01_0");

    }
    public static void readshapeFileByLine(String strFile){
        try {
            File file = new File(strFile);
            BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
            String strLine = null;
            int lineCount = 1;

            while(null != (strLine = bufferedReader.readLine())){
                List<Point2D.Double> points = new ArrayList<Point2D.Double>();
                String [] linearr = strLine.split(" ");
                for(String s1 : linearr){
                    String [] singlearr = s1.split(",");
                    Point2D.Double pointNot = new Point2D.Double(Double.parseDouble(singlearr[0]), Double.parseDouble(singlearr[1]));
                    points.add(pointNot);
                }
                //System.out.println(strLine);
                pointslist.add(points);
                lineCount++;
            }
            System.out.println(lineCount);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    /*获取文件的路径*/
    public static void printFile(File file) {
        if (file.isFile()) {
            System.out.println("您给定的是一个文件"); // 判断给定目录是否是一个合法的目录，如果不是，输出提示
        } else {
            File[] fileLists = file.listFiles(); // 如果是目录，获取该目录下的内容集合
            for (int i = 0; i < fileLists.length; i++) {
                System.out.println(fileLists[i].getName());
                // 循环遍历这个集合内容
                File[] subfileLists = fileLists[i].listFiles();
                for (int j = 0; j < subfileLists.length; j++){
                    //System.out.println(subfileLists[j].getName());
                    File[] ssubfileLists = subfileLists[j].listFiles();
                    for (int k = 0; k < ssubfileLists.length; k++){
                        //readFileByLine();
                        System.out.println("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data\\"+fileLists[i].getName()+'\\'+subfileLists[j].getName()+'\\'+ssubfileLists[k].getName());
                        readFileByLine("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data\\"+fileLists[i].getName()+'\\'+subfileLists[j].getName()+'\\'+ssubfileLists[k].getName(),"C:\\Users\\11838\\IdeaProjects\\SuanFa\\Data\\"+fileLists[i].getName());
                    }

                }

            }
        }
    }

    /**
     * 按行读取shape文件
     * @param strFile
     */


    public static void readFileByLine(String strFile,String finalwritename){
        String geton_ymd,getoff_ymd;
        String geton_time,getoff_time;
        int getoff_timesnap,geton_timesnap;
        int get_on_TAZ=0,get_off_TAZ=0;
        try {
            File file = new File(strFile);
            BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
            String strLine = null;
            File writefile = new File(finalwritename);
            FileWriter fw = new FileWriter(writefile,true);


            while(null != (strLine = bufferedReader.readLine())){
                //System.out.println(strLine);  2019-01-01 00:03:20,粤B0C8P1,126419,1546271953000,1514736167000,13.0,3.38,1.64,0.0090,0:0:26,1,ffffffffffffffffffff,0.0,114.051615,22.529625,114.04954666666667,22.537385
                String [] linearr = strLine.split(",");
                //System.out.println(linearr.length); 17


                if (113.775 <= Double.parseDouble(linearr[13]) && Double.parseDouble(linearr[13])<= 114.629 &&
                   22.443 <= Double.parseDouble(linearr[14]) && Double.parseDouble(linearr[14])<= 22.855  &&
                   113.775 <= Double.parseDouble(linearr[15]) && Double.parseDouble(linearr[15])<= 114.629 &&
                   22.443 <= Double.parseDouble(linearr[16]) && Double.parseDouble(linearr[16])<= 22.855){

                    geton_time = stampToDate(Long.parseLong(linearr[3]));
                    //System.out.println(geton_time);20181231 235913
                    //System.out.println(geton_time.substring(9,11));23

                    geton_ymd = geton_time.substring(0,8);
                    if(Integer.parseInt(geton_time.substring(11,13))>=30){
                        int temp = Integer.parseInt(geton_time.substring(11,13));
                        geton_timesnap = Integer.parseInt(geton_time.substring(9,11)) * 2 + 1;
                    }else{
                        geton_timesnap = Integer.parseInt(geton_time.substring(9,11)) * 2;
                    }
                    getoff_time = stampToDate(Long.parseLong(linearr[4]));
                    //System.out.println(geton_time);20181231 235913
                    //System.out.println(geton_time.substring(9,11));23

                    getoff_ymd = getoff_time.substring(0,8);

                    if(Integer.parseInt(getoff_time.substring(11,13))>=30){
                        getoff_timesnap = Integer.parseInt(getoff_time.substring(9,11)) * 2 + 1;
                    }else{
                        getoff_timesnap = Integer.parseInt(getoff_time.substring(9,11)) * 2;
                    }
//                    System.out.println(geton_time);
//                    System.out.println(getoff_time);
                    Point2D.Double position = new Point2D.Double(Double.parseDouble(linearr[13]), Double.parseDouble(linearr[14]));
                    for (int i = 0; i < pointslist.size(); i++) {
                       if(isPtInPolygon(position,pointslist.get(i))){
                           get_on_TAZ = i;
                           break;
                       }
                    }
                    position = new Point2D.Double(Double.parseDouble(linearr[15]), Double.parseDouble(linearr[16]));
                    for (int i = 0; i < pointslist.size(); i++) {
                        if(isPtInPolygon(position,pointslist.get(i))){
                            get_off_TAZ = i;

                            break;
                        }
                    }
                    fw.write(linearr[1]+","+geton_ymd+","+geton_timesnap+","+getoff_ymd+","+getoff_timesnap+","+get_on_TAZ+","+get_off_TAZ+'\n');
                }

            }
            fw.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    /*
     * 将时间戳转换为时间
     */
    public static String stampToDate(long stime){
        SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMdd HHmmss");
        String sd = sdf.format(Long.parseLong(String.valueOf(stime)));
        return sd;
    }

    public static boolean isPtInPolygon (Point2D.Double point , List<Point2D.Double> polygon) {

        int iSum,iIndex;
        double dLon1 , dLon2 , dLat1 , dLat2 , dLon;
        int size = polygon.size();
        iSum = 0;
        for (iIndex = 0; iIndex<size; iIndex++) {
            if (iIndex == size - 1) {
                dLon1 = polygon.get(iIndex).getX();
                dLat1 = polygon.get(iIndex).getY();
                dLon2 = polygon.get(0).getX();
                dLat2 = polygon.get(0).getY();
            } else {
                dLon1 = polygon.get(iIndex).getX();
                dLat1 = polygon.get(iIndex).getY();
                dLon2 = polygon.get(iIndex + 1).getX();
                dLat2 = polygon.get(iIndex + 1).getY();
            }
            // 以下语句判断A点是否在边的两端点的水平平行线之间，在则可能有交点，开始判断交点是否在左射线上
            if (((point.y >= dLat1) && (point.y < dLat2))
                    || ((point.y >= dLat2) && (point.y < dLat1))) {
                if (Math.abs(dLat1 - dLat2) > 0) {
                    //得到 A点向左射线与边的交点的x坐标：
                    dLon = dLon1 - ((dLon1 - dLon2) * (dLat1 - point.y) ) / (dLat1 - dLat2);
                    // 如果交点在A点左侧（说明是做射线与 边的交点），则射线与边的全部交点数加一：
                    if (dLon < point.x) {
                        iSum++;
                    }
                }
            }
        }
        return (iSum % 2) != 0;
    }

}
