package com.capstoneproject.c22ps159.pake.ui.addcar

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.view.View
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import androidx.core.view.isInvisible
import com.capstoneproject.c22ps159.pake.R
import com.capstoneproject.c22ps159.pake.data.helper.Utils
import com.capstoneproject.c22ps159.pake.databinding.ActivityAddCarBinding
import java.io.File

class AddCarActivity : AppCompatActivity() {
    private lateinit var binding: ActivityAddCarBinding

    private lateinit var currentPhotoPath: String

    private var getFile: File? = null

    companion object {

        const val CAMERA_X_RESULT = 200
        private const val TAG = "AddCarActivity"

        private val REQUIRED_PERMISSIONS = arrayOf(Manifest.permission.CAMERA)
        private const val REQUEST_CODE_PERMISSIONS = 10
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (!allPermissionsGranted()) {
                Toast.makeText(
                    this,
                    getString(R.string.camera_not_allowed),
                    Toast.LENGTH_SHORT
                ).show()
                finish()
            }
        }
    }

    private fun allPermissionsGranted() = REQUIRED_PERMISSIONS.all {
        ContextCompat.checkSelfPermission(baseContext, it) == PackageManager.PERMISSION_GRANTED
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAddCarBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.title = getString(R.string.AddCarActivity)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)


        if (!allPermissionsGranted()) {
            ActivityCompat.requestPermissions(
                this,
                REQUIRED_PERMISSIONS,
                REQUEST_CODE_PERMISSIONS
            )
        }

        binding.cameraButton.setOnClickListener {startIntentCamera() }
        binding.galleryButton.setOnClickListener { startGallery() }

    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    private fun startIntentCamera() {
        val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        intent.resolveActivity(packageManager)

        Utils.createTempFile(application).also {
            val photoURI: Uri = FileProvider.getUriForFile(
                this,
                "com.capstoneproject.c22ps159.pake.ui.addcar",
                it
            )
            currentPhotoPath = it.absolutePath
            intent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI)
            launcherIntentCamera.launch(intent)
        }
    }

    private fun startGallery() {
        val intent = Intent()
        intent.action = Intent.ACTION_GET_CONTENT
        intent.type = "image/*"
        val chooser = Intent.createChooser(intent, "Choose a Picture")
        launcherIntentGallery.launch(chooser)
    }

    private val launcherIntentGallery = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) {
        if (it.resultCode == RESULT_OK) {
            val selectedImg: Uri = it.data?.data as Uri
            val myFile = Utils.uriToFile(selectedImg, this)
            getFile = myFile
            binding.dummy.setImageURI(selectedImg)
            binding.addImage.visibility = View.GONE
        }
    }

    private val launcherIntentCamera = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) {
        if (it.resultCode == RESULT_OK) {
            val myFile = File(currentPhotoPath)
            val result =  BitmapFactory.decodeFile(myFile.path)

            binding.dummy.setImageBitmap(result)
            binding.addImage.visibility = View.GONE

        }
    }
}