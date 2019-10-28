package com.abc.currencycovertor;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public void convertFunction(View view){
        EditText Numberfield=(EditText)findViewById(R.id.Currency);
        String str=Numberfield.getText().toString();
        double d=Double.parseDouble(str);
        double d1=d*0.014;
        Toast.makeText(this, "$"+String.format("%.2f",d1), Toast.LENGTH_SHORT).show();
        Log.i("Converted your currency","$"+String.format("%.2f",d1));
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
