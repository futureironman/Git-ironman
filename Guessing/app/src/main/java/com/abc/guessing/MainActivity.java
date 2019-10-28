package com.abc.guessing;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    public void clickOne(View view){
        Log.i("Info","You are going to be a richest person on this planet");
    }
    public void clickTwo(View view){
        Log.i("Info","You are going to be a game company owner.");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
