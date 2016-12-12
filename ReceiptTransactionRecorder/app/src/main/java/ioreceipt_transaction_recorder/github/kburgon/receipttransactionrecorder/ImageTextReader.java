package ioreceipt_transaction_recorder.github.kburgon.receipttransactionrecorder;

/**
 * Created by Kevin Burgon on 12/5/16.
 */

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.vision.v1.Vision;
import com.google.api.services.vision.v1.VisionScopes;
import com.google.api.services.vision.v1.model.AnnotateImageRequest;
import com.google.api.services.vision.v1.model.AnnotateImageResponse;
import com.google.api.services.vision.v1.model.BatchAnnotateImagesRequest;
import com.google.api.services.vision.v1.model.BatchAnnotateImagesResponse;
import com.google.api.services.vision.v1.model.EntityAnnotation;
import com.google.api.services.vision.v1.model.Feature;
import com.google.api.services.vision.v1.model.Image;
//import com.google.common.collect.ImmutableList;

//import java.io.IOException;
//import java.security.GeneralSecurityException;
//import java.util.List;
//
//public class ImageTextReader {
//    /**
//     * Connects to the Vision API using Application Default Credentials.
//     */
//    public static Vision getVisionService() throws IOException, GeneralSecurityException {
//        GoogleCredential credential =
//                GoogleCredential.getApplicationDefault().createScoped(VisionScopes.all());
//        JsonFactory jsonFactory = JacksonFactory.getDefaultInstance();
//        return new Vision.Builder(GoogleNetHttpTransport.newTrustedTransport(), jsonFactory, credential)
//                .setApplicationName(APPLICATION_NAME)
//                .build();
//    }
//}
