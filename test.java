import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Random;
import java.util.Set;
import java.util.TreeSet;

import com.sun.org.apache.xpath.internal.SourceTree;

import java.util.List;

class Test {
    public static void main(String[] args) {
        Test test = new Test();
        test.getWords();
    }
    
    public List<Character[][]> getWords() {
        List<Character[][]> wordsToShow = new ArrayList<>();
        List<String> puzzleWords = new ArrayList<>();
        Random random = new Random();
        Set<Integer> setWordIndex = new TreeSet<>();
        Set<Integer> setWordArrangement = new TreeSet<>();
        
        while (setWordIndex.size() < 9) {
            setWordIndex.add(random.nextInt(58447));
        }
        
        while (setWordArrangement.size() < 9) {
            setWordArrangement.add(random.nextInt(784));
        }
        
        
        try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(
            "/media/vinay/New_Ubuntu/MSCS-Assignments/CS5520_MAD/vinaysingh-5520/NUMAD19SUVinaySingh/app/src/main/assets/wordlist_nine.txt")))) {
            String line;
            int lineNumber = 0;
            for (int key : setWordIndex) {
                while ((line = br.readLine()) != null && lineNumber != key) {
                    ++lineNumber;
                }
                if (line!= null) {
                    puzzleWords.add(line.trim().toLowerCase());
                }
            }
        } catch (IOException e) {
        }
        List<String> arrangementOrder = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(
            "/media/vinay/New_Ubuntu/MSCS-Assignments/CS5520_MAD/vinaysingh-5520/NUMAD19SUVinaySingh/app/src/main/assets/possible_arrangements.txt")))) {
            String line;
            int lineNumber = 0;
            for (int key : setWordArrangement) {
                while ((line = br.readLine()) != null && lineNumber != key) {
                    ++lineNumber;
                }
                if (line != null) {
                    arrangementOrder.add(line.trim().toLowerCase());
                }
                if (arrangementOrder.size() >= setWordArrangement.size()) {
                    break;
                }
            }
        } catch (IOException e) {
        }
        for (int i = 0; i < 9; ++i) {
            String[] order = arrangementOrder.get(i).split(" ");
            int[] index = new int[order.length];
            for (int j = 0; j < order.length; j++) {
                index[j] = Integer.valueOf(order[j]);
            }
            int colCount = (int) Math.sqrt(9);
            Character [][] jumbledWordOrder = new Character[colCount][colCount];
            int  ptr = 0;
            
            for (int m = 0; m < colCount; m++) {
                for (int n = 0; n < colCount; n++) {
                    System.out.print(puzzleWords.get(i).charAt(index[ptr]));
                    jumbledWordOrder[m][n] = puzzleWords.get(i).charAt(index[ptr++]);
                }
            }
            System.out.println();
            wordsToShow.add(jumbledWordOrder);
        }
        System.out.println(wordsToShow);
        return wordsToShow;        
    }
}
