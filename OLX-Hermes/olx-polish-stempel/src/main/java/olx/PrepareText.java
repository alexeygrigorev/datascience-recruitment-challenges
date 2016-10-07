package olx;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.FileUtils;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.pl.PolishAnalyzer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;

import com.fasterxml.jackson.jr.ob.JSON;

public class PrepareText {

    private static final PolishAnalyzer POLISH_ANALYZER = new PolishAnalyzer();

    public static void main(String[] args) throws IOException {
        File input = new File("/home/agrigorev/tmp/data/olx/train.json");
        File output = new File("/home/agrigorev/tmp/data/olx/train-stemmed.json");

        List<String> lines = FileUtils.readLines(input, "UTF-8");

        PrintWriter pw = new PrintWriter(output, "UTF-8");

        lines.stream()
              .map(l -> read(l))
              .map(l -> stem(l))
              .map(l -> toJson(l))
              .forEach(pw::println);

        pw.flush();
        pw.close();
    }

    private static String normalize(String ex) {
        try {
            TokenStream tokenStream = POLISH_ANALYZER.tokenStream("default", ex);
            tokenStream.reset();

            List<String> result = new ArrayList<String>();
            while (tokenStream.incrementToken()) {
                CharTermAttribute attr = tokenStream.getAttribute(CharTermAttribute.class);
                result.add(attr.toString());
            }

            tokenStream.close();
            return String.join(" ", result);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static Line stem(Line line) {
        String description = line.getDescription();
        description = normalize(description);
        line.setDescription(description);

        String title = line.getTitle();
        title = normalize(title);
        line.setTitle(title);

        return line;
    }

    public static Line read(String line) {
        try {
            return JSON.std.beanFrom(Line.class, line);
        } catch (IOException e) {
            throw new RuntimeException();
        }
    }

    private static String toJson(Line l) {
        try {
            return JSON.std.asString(l);
        } catch (IOException e) {
            throw new RuntimeException();
        }
    }

    static class Line {
        private String arrival_date;
        private String user_created_at;
        private String description;
        private String title;
        private String price_type;
        private BigDecimal price;
        private double label;
        private int category_id;

        public String getArrival_date() {
            return arrival_date;
        }

        public void setArrival_date(String arrival_date) {
            this.arrival_date = arrival_date;
        }

        public String getUser_created_at() {
            return user_created_at;
        }

        public void setUser_created_at(String user_created_at) {
            this.user_created_at = user_created_at;
        }

        public String getDescription() {
            return description;
        }

        public void setDescription(String description) {
            this.description = description;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public String getPrice_type() {
            return price_type;
        }

        public void setPrice_type(String price_type) {
            this.price_type = price_type;
        }

        public BigDecimal getPrice() {
            return price;
        }

        public void setPrice(BigDecimal price) {
            this.price = price;
        }

        public double getLabel() {
            return label;
        }

        public void setLabel(double label) {
            this.label = label;
        }

        public int getCategory_id() {
            return category_id;
        }

        public void setCategory_id(int category_id) {
            this.category_id = category_id;
        }

    }

}
