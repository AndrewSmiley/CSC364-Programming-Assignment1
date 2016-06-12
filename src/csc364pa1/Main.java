package csc364pa1;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String data= input.nextLine();
        HashMap<Integer, Character> history = new HashMap<Integer, Character>();
        int longestSequence = 0;
        int previousscores[]= new int[data.length()];
        for(int i =0; i < data.length(); i++){
            //handle base case
            if(i==0){
                previousscores[i] = -1;
                history.put(i, data.charAt(i));
                longestSequence++;
            }else{
                //do the check to see if it's less than the last char we were dealing with
                if( data.charAt(i) < data.charAt(i-1)){
                    int j = longestSequence;
                    //here's our n^2
                    while(j > 0){
                        if(history.get(j) < data.charAt(i)){
                            history.put(j, data.charAt(i));
                            previousscores[i]++;
                            break;
                        }

                    }
                }
            }


        }
    }
}
