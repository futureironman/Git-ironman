package com.abc.facebook;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    public void loginFunction(View view){
        EditText Username=(EditText)findViewById(R.id.Username);
        EditText Password=(EditText)findViewById(R.id.Password);
        Log.i("Username",Username.getText().toString());
        Log.i("Password",Password.getText().toString());
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
