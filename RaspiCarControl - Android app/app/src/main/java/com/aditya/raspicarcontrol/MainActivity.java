package com.aditya.raspicarcontrol;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    DatabaseReference databaseReference;
    ValueEventListener valueEventListener;
    Button moveForward, moveBackward, turnRight, turnLeft, stopRaspiCar;
    TextView carStatus;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        moveForward = (Button) findViewById(R.id.moveForward);
        moveBackward = (Button) findViewById(R.id.moveBackward);
        turnLeft = (Button) findViewById(R.id.turnLeft);
        turnRight = (Button) findViewById(R.id.turnRight);
        stopRaspiCar = (Button) findViewById(R.id.stopCar);

        updateCarState();


        moveForward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState").setValue("W").addOnCompleteListener(new OnCompleteListener<Void>() {
                   @Override
                   public void onComplete(@NonNull Task<Void> task) {
                       updateCarState();
                   }
               }).addOnFailureListener(new OnFailureListener() {
                   @Override
                   public void onFailure(@NonNull Exception e) {

                   }
               });
            }
        });


        turnRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState").setValue("A").addOnCompleteListener(new OnCompleteListener<Void>() {
                    @Override
                    public void onComplete(@NonNull Task<Void> task) {
                        updateCarState();
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {

                    }
                });
            }
        });


        turnLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState").setValue("D").addOnCompleteListener(new OnCompleteListener<Void>() {
                    @Override
                    public void onComplete(@NonNull Task<Void> task) {
                        updateCarState();
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {

                    }
                });
            }
        });

        moveBackward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState").setValue("S").addOnCompleteListener(new OnCompleteListener<Void>() {
                    @Override
                    public void onComplete(@NonNull Task<Void> task) {
                        updateCarState();
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {

                    }
                });
            }
        });


        stopRaspiCar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState").setValue("Stationary").addOnCompleteListener(new OnCompleteListener<Void>() {
                    @Override
                    public void onComplete(@NonNull Task<Void> task) {
                        updateCarState();
                      //  finish();
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {

                    }
                });
            }
        });

    }

    public  void  updateCarState(){
        carStatus = (TextView) findViewById(R.id.carState);
        databaseReference = FirebaseDatabase.getInstance().getReference().child("raspi-car").child("carState");
        databaseReference.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if(snapshot.getValue().toString().equals("W")) {
                    carStatus.setText("Car State: Moving forward");
                }else if(snapshot.getValue().toString().equals("S")){
                    carStatus.setText("Car State: Moving backward");
                }else if(snapshot.getValue().toString().equals("D")){
                    carStatus.setText("Car State: Moving Left");
                }else if(snapshot.getValue().toString().equals("A")){
                    carStatus.setText("Car State: Moving Right");
                }else {
                    carStatus.setText("Car State: Stationary");
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });


    }

}